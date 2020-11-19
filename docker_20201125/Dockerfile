FROM python:3.8

LABEL maintainer="Orozco Hsu"\
      name="ntuhs_2020_docker"\
	  version="0.1"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
