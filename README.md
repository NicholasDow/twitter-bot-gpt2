# twitter-bot
I'm keeping all my twitter bot related stuff here.

Things, this has
- Twitter bot scripts
- GPT2 tweet generation script
  - model file here:
  - https://drive.google.com/file/d/1Hmpwr87FZfbT9I-PKhV2Jn6nHtv2VVf5/view?usp=sharing
- tweets texts that I generated
- A twint script that helps downloads and processes tweets beyond 3200 api rate limit that twitter put in place since the election
- Collected tweets from accounts that I thought would make for good generation. Feel free to download any of them and use for yourself. They don't have links, some of them might include replies. if you don't want replies then run the script again on the account.

# To DO

Work on the twitter stream so that you auto follow accounts that mention specific key words and have fewwer than 1000 followers

When your account follows them, give them a certain amount of time to follow you back.

If they don't follow you in the time span then un follow them and blacklist them on the following command

I would like to be able to train tweet generation on geographic locations pretaining to specific topics rather than particular users. I wonder if anything funny can come out of that. I think that I will see if collecting tweets from around comedy bars after 7pm on weekends will produce a generator that makes funny things.

I would also like to generate tweets for the average harvard student. I will collect geo tweets from leverett once the pandemic is over

# Notes

## GPT2
- the ideal loss for funny tweets is somewhere around 1.25. 
- running on a 124M+ is only nescessary if you have ALOT of data.

## Twint
- You have to use the github version of twint instead of the pip version of twint if you want to run it in a python script rather than in a command line, at least as of writing this
- I think there will be more issues with twint as twitter tries to crack down more
- The issue with downloading tweets
(note to self, when you next have to go through the process of installing, put links to the forums that had the solutions to problems encountered)(issues with script)(issues with twint)
