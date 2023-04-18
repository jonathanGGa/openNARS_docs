"""
 * The MIT License
 *
 * Copyright 2023 The OpenNARS authors.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 * """

import sys
from NAL import *
from Prompts import *
import openai
openai.api_key = "YOUR_KEY"

IncludeGPTKnowledge = False or "IncludeGPTKnowledge" in sys.argv #Whether it should be allowed to consider GPT's knowledge too
PrintInputSentence = False
PrintTruthValues = True
PrintMemoryUpdates = False
PrintGPTPrompt = False

memory = {} #the NARS-style long-term memory

def attention_buffer(attention_buf_target_size = 20):
    attention_buf=[]
    relevant_item_list = list(memory.items())
    #find attention_buf_target_size/2 newest items:
    relevant_item_list.sort(key=lambda x: -x[1][0])
    attention_buf += reversed(relevant_item_list[0:int(attention_buf_target_size/2)]) #newer comes later in prompt
    #find additional attention_buf_target_size/2 useful items which were not already part of the newest
    relevant_item_list.sort(key=lambda x: -x[1][1])
    for x in attention_buf:
        if x in relevant_item_list:
            relevant_item_list.remove(x) #so we won't select it as it is already part of mem
    i = 0
    while len(attention_buf) < attention_buf_target_size and i < len(relevant_item_list):
        attention_buf = [relevant_item_list[i]] + attention_buf
        i += 1
    return attention_buf

def generate_prompt(prompt_start, prompt_end):
    prompt_memory = ""
    buf = attention_buffer()
    if len(buf) == 0:
        prompt_memory = "EMPTY!"
    for i,x in enumerate(buf):
        (f,c) = x[1][2]
        flags = []
        if c < 0.5:
            flags.append("hypothetically")
        else:
            flags.append("knowingly")
        if f < 0.3:
            flags.append("False")
        elif f > 0.7:
            flags.append("True")
        else:
            flags.append("Contradictory")
        certainty = Truth_Expectation((f,c))
        truthtype = '"' + " ".join(flags) + '"'
        prompt_memory += f"i={i}: {x[0]}. truthtype={truthtype} certainty={certainty}\n"
    return prompt_start + prompt_memory + prompt_end

currentTime = 0
def NAL_infer_to_memory(cmd, userQuestion):
    global memory
    for x in cmd:
        truth = (1.0, 0.9)
        systemQuestion = x.startswith("Question(")
        if userQuestion or systemQuestion:
            print(x)
        isNegated = False
        if x.startswith("Negated"):
            isNegated = True
            x = x[7:]
            truth = (0.0, 0.9)
        isDeduction = x.startswith("Deduce(")
        isInduction = x.startswith("Induce(")
        isAbduction = x.startswith("Abduce(")
        isInput = x.startswith("Claim(")
        if (isDeduction or isInduction or isAbduction or isInput) and ")" in x:
            arg = x.split("(")[1].split(")")[0].replace('"','').replace("'","").replace(".", "").lower()
            if isDeduction or isInduction or isAbduction:
                statements = [x.strip().replace(".", "") for x in arg.split(", ")]
                if len(statements) != 3:
                    continue
                if statements[0] not in memory or statements[1] not in memory:
                    continue
                if isDeduction:
                    truth = Truth_Deduction(memory[statements[0]][2], memory[statements[1]][2])
                elif isInduction:
                    truth = Truth_Induction(memory[statements[0]][2], memory[statements[1]][2])
                elif isAbduction:
                    truth = Truth_Abduction(memory[statements[0]][2], memory[statements[1]][2])
                arg = statements[2] #the conclusion is to pbe put to memory
            useRevision = True
            if arg in memory and isDeduction:
                useRevision = False #use choice here before we have stamps
            if isDeduction or isInduction or isAbduction or isInput:
                if PrintTruthValues:
                    print(f"{x} truth={truth}")
                else:
                    print(x)
            if arg not in memory:
                memory[arg] = (0, 0, (0.5, 0.0))
            if arg in memory:
                lastUsed, useCount, TV = memory[arg]
                memory[arg] = (currentTime, useCount+1, Truth_Revision(TV, truth) if useRevision else Truth_Choice(TV, truth))
                if PrintMemoryUpdates: print("//UPDATED", arg, memory[arg])

while True:
    try:
        inp = input().rstrip("\n")
    except:
        exit(0)
    if PrintInputSentence: print("Input:", inp)
    if inp.startswith("*volume="):
        continue
    if inp.startswith("*prompt"):
        print(generate_prompt("",""))
        continue
    if inp.startswith("*memory"):
        for x in memory.items():
            print(x)
        continue
    if inp.startswith("*buffer"):
        attention_buf = attention_buffer()
        for x in attention_buf:
            print(x)
        continue
    if inp.endswith("?"):
        isQuestion = True
        send_prompt = generate_prompt(question_prompt_start, "\nThe question: ") + inp[:-1] + (question_prompt_end_alternative if IncludeGPTKnowledge else question_prompt_end)
    else:
        isQuestion = False
        send_prompt = generate_prompt(belief_prompt_start, "\nThe sentence: ") + inp + belief_prompt_end
        currentTime += 1
    if PrintGPTPrompt: print("vvvvSTART PROMPT", send_prompt, "\n^^^^END PROMPT")
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[ {"role": "user", "content": send_prompt}], max_tokens=200, temperature=0)
    NAL_infer_to_memory(response['choices'][0]['message']['content'].split("\n"), isQuestion)
