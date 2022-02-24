FROM python:3 as builder
COPY . .
RUN pip install --upgrade build
RUN python -m build

FROM python:3-alpine
COPY --from=builder /dist/* dist/
RUN pip install dist/*-py2.py3-none-any.whl
CMD ["salesforce-exporter", "start-server"]
