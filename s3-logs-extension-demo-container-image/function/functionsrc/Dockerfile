FROM log-extension-image:latest AS layer
FROM public.ecr.aws/lambda/python:3.8
# Layer code
WORKDIR /opt
COPY --from=layer /opt/ .

# Function code
WORKDIR /var/task
COPY app.py .

RUN chmod +x /opt/extensions/logs_api_http_extension.py
CMD ["app.lambda_handler"]
