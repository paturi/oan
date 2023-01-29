import json
path = "D:\projects\oan\data"
inf = open(path+"\even.json", 'r', encoding='UTF-8-sig')
outf = open(path+"\even1.jsonl", 'w', encoding='UTF-8')
for line in inf:
    tmp = dict()
    data = json.loads(line)
    prompt = data["prompt"]
    prompt = prompt+" You say ->"
    tmp["prompt"] = prompt
    completion = data["completion"]
    completion = " "+completion
    print(completion)
    tmp["completion"] = completion
    json.dump(tmp, outf)
    outf.write('\n')
outf.close()
inf.close()
    #print(data["prompt"], data["completion"])