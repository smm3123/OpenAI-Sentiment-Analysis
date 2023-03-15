# OpenAI-Sentiment-Analysis

Quick prototype with the `OpenAI` API to see how it handles sentiment analysis. This program tests out how it handles sentiment analysis on a scale of 1-5, going from most negative to most positive.

Example output:
```
Prompt:
Determine what the sentiment of each of these responses is on a scale of 1 - 5, where 1 is the most negative, 3 is neutral, and 5 is positive:
1. Could do better work next time, currently still progress that needs to be made
2. Did a good job in the classroom, students listened to them
3. Amazing work, keep it up!
4. Not good, not bad
5. While this was enjoyable enough, it wasn't really great...in fact, I'd go so far as to say it wasn't great at all

Sentiments:
1. Could do better work next time, currently still progress that needs to be made -> 2
2. Did a good job in the classroom, students listened to them -> 5
3. Amazing work, keep it up! -> 5
4. Not good, not bad -> 3
5. While this was enjoyable enough, it wasn't really great...in fact, I'd go so far as to say it wasn't great at all -> 1

Response:
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "text": "\n1. 2\n2. 5\n3. 5\n4. 3\n5. 1"
    }
  ],
  "created": 1678857297,
  "id": "x",
  "model": "text-davinci-003",
  "object": "text_completion",
  "usage": {
    "completion_tokens": 20,
    "prompt_tokens": 120,
    "total_tokens": 140
  }
}
```
