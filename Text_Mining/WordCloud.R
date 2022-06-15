library(wordcloud)
library(RColorBrewer)
library(wordcloud2)
library(tm)
library(dplyr)

job <- "jobs.txt"
text <- readLines(job)
docs <- Corpus(VectorSource(text))
inspect(docs)

#change any characters matching in tm_map to a space
toSpace <- content_transformer(function (x , pattern ) gsub(pattern, " ", x))

clean_job <- docs %>%
  tm_map(removeNumbers) %>%
  tm_map(removePunctuation) %>%
  tm_map(stripWhitespace) %>%
  tm_map(toSpace, "/") %>%
  #Double backslash \\ is necessary for brackets/parantheses to prevent error                               
  tm_map(toSpace, "\\{") %>%                                
  tm_map(toSpace, "\\}") %>%
  tm_map(toSpace, ":") %>%
  tm_map(toSpace, ";") %>%
  tm_map(toSpace, '"') %>%
  tm_map(toSpace, "\u00a0\u00a0\u00a0") %>%
  tm_map(toSpace, "$") %>%
  tm_map(toSpace, "\\W") %>% #all non-words
  #Can customize removeWords                               
  tm_map(removeWords, c("gsk", "role", "you", "the", "into", "will", "job", "use", "large")) %>% 
  tm_map(stripWhitespace) %>%
  tm_map(content_transformer(tolower)) %>%
  tm_map(removeWords, stopwords("english"))
dtm <- TermDocumentMatrix(clean_job)
m <- as.matrix(dtm)
v <- sort(rowSums(m),decreasing=TRUE)
d <- data.frame(word = names(v),freq=v)

#Check for 10 more frequently used words)
head(d, 10) 

set.seed(1234) #for reproducibility
#Can customize word cloud graphics                               
wordcloud(words = d$word, freq = d$freq, min.freq = 1, scale = c(2,1),
          max.words=75, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
