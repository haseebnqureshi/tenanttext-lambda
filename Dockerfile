FROM public.ecr.aws/lambda/python:3.11

# Install build dependencies
RUN yum install -y gcc gcc-c++ python3-devel

COPY requirements.txt .

# Install with --no-cache-dir to ensure fresh builds
RUN pip install --no-cache-dir -r requirements.txt -t python/lib/python3.11/site-packages/

CMD ["cp", "-r", "python", "/output/"] 