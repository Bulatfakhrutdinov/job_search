# Job Search

A system that helps job seekers find relevant job vacancies based on their text descriptions.

**Value**  
Time-saving in finding suitable job vacancies.

**Target Audience**  
Job seekers without experience, students.

**ML Task**  
Job vacancy search by semantic similarity to text query (IR task).

**Attention**

Due to GitHub restrictions, it is not possible to download the original dataset. I took the dataset from the [link](https://www.kaggle.com/datasets/etietopabraham/jobs-raw-data). The dataset should be located in the 'data' folder and named job_postings.csv for proper operation

### Requirements
- Docker
- Docker Compose


Clone the repository:
```
git clone https://github.com/Bulatfakhrutdinov/job_search.git
```

```
cd job_search
```

Download [dataset](https://www.kaggle.com/datasets/etietopabraham/jobs-raw-data) and create a backend/job_dataset folder and put the dataset in it.

Now you can run the API with:
```
docker compose up -d
```
