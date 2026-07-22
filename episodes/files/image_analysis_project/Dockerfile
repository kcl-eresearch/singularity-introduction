FROM python:3.12
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt
RUN mkdir /scripts
COPY scripts/process_images.py /scripts/
COPY scripts/analyse_images.py /scripts/
RUN chmod +x /scripts/*.py
# add /scripts folder to the PATH
ENV PATH=/scripts:$PATH
CMD ["python", "--version"]
