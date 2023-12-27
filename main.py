from youtube_transcript_api import YouTubeTranscriptApi
import openai 

video_id = "-eqMHB8Ctuo&t=105s"

res = YouTubeTranscriptApi.get_transcript(video_id, languages=['zh-Hans'])

batch_size = 20 * 5
all_list = []
tmp = 0
tmp_sentence = ""
for sentence in res:
	if tmp < batch_size:
		if tmp != 0:
			tmp_sentence += ", "
		tmp_sentence += sentence.get("text")
		tmp += 1
	else:
		all_list.append(tmp_sentence)
		tmp_sentence = ""
		tmp = 0

# print(all_list)

import os
import openai 
# export OPENAI_API_KEY='your-api-key-here'
my_api_key = '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'
os.environ['OPENAI_API_KEY'] = my_api_key

client = openai.OpenAI()


for item in all_list:
	print(item)
	completion = client.chat.completions.create(
	  model="gpt-3.5-turbo",
	  messages=[
	    # {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
	    {"role": "user", "content": f"请以要点形式总结这句话： {item}"}
	  ]
	)

	print(completion.choices[0].message)

