# base Docker image
FROM python 3.12.2

# Copy uv binary from official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv/bin/

# Setting up the working directory
WORKDIR /simple_pipeline

# add virtual environment to PATH
ENV PATH="/data_engineering/.venv/Scripts:${PATH}"

# set up the image by installing dependencies or prerequisites
# in the requirements.txt file
COPY "pyproject.toml" "uv.lock" "pyproject.toml"
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# ensuring reproducible builds by using uv to install dependencies
RUN uv sync --lockfile uv.lock --install --no-dev

# copy the scripts to the container
COPY . .

# run the script
CMD ["python", "main.py"] # ENTRYPOINT ["python", "main.py"]