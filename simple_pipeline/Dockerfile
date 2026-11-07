# base Docker image
FROM python 3.12.2

# set up the image by installing dependencies or prerequisites
# in the requirements.txt file
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Setting up the working directory
WORKDIR /simple_pipeline

# copy the scripts to the container
COPY . .

# run the script
CMD ["python", "main.py"] # ENTRYPOINT ["python", "main.py"]