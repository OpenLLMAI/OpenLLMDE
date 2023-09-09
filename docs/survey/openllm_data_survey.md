# LLM DATA SURVEY

## 1.Data Tasks

### 1.1 Dataset tasks 

| Data Task(with url) | Intro | State(0:TODO, 1:doing, 2:done) |
| ------------------- | ----- | ------------------------------ |
| alpaca              |       | 1                              |
| vicuna              |       | 0                              |
|                     |       |                                |



### 1.2 Data Engineering tasks 

| DE Task(with url) | Intro | State(0:TODO, 1:doing, 2:don |
| ----------------- | ----- | ---------------------------- |
| GPT3              |       | 0                            |
| T5                |       | 0                            |
| LLaMA             |       | 0                            |
|                   |       |                              |



## 2.Data survey

### 2.1 Pretrain Data Survey

| data | lng  | size | token | avg_len | src  | quality_human | quality_auto | Key idea | Notes |
| ---- | ---- | ---- | ----- | ------- | ---- | ------------- | ------------ | -------- | ----- |
| Pile | en   |      |       |         |      |               |              |          |       |
|      |      |      |       |         |      |               |              |          |       |

### 2.2 SFT Data Survey

| data   | lng  | size | token | avg_len | query_src | answer_src | quality_human | quality_auto | Key idea | Notes |
| ------ | ---- | ---- | ----- | ------- | --------- | ---------- | ------------- | ------------ | -------- | ----- |
| alpaca | en   | ~50k |       |         |           |            |               |              |          |       |
|        |      |      |       |         |           |            |               |              |          |       |

### 2.3 RLHF Data Survey

| data | lng  | size | token | avg_len | query_src | answer_src | quality_human | quality_auto | Key idea | Notes |
| ---- | ---- | ---- | ----- | ------- | --------- | ---------- | ------------- | ------------ | -------- | ----- |
|      |      |      |       |         |           |            |               |              |          |       |
|      |      |      |       |         |           |            |               |              |          |       |



## 3. Data Engeneering Survey

3.1 DE by Model

| Model | Methods | key idea | Notes |
| ----- | ------- | -------- | ----- |
| GPT1  |         |          |       |
| GPT2  |         |          |       |
| GPT3  |         |          |       |
|       |         |          |       |



3.2 DE by Method

| DE Method                             | src  | tool | key idea | State | details |
| ------------------------------------- | ---- | ---- | -------- | ----- | ------- |
| Coarse-grained quality classification |      |      |          | 0     |         |
| Fine-grained quality score            |      |      |          |       |         |
| 0-shot cls                            |      |      |          |       |         |
| Difficulty rating                     |      |      |          |       |         |
|                                       |      |      |          |       |         |
