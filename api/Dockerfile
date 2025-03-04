FROM python:3.13.2-slim-bookworm AS development

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY pyproject.toml ./

RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.local/bin/:$PATH"

RUN uv sync

COPY . /app

FROM development AS prod

COPY --from=development /app /app

RUN uv sync --no-dev

EXPOSE 8000
CMD ["uv", "run", "main.py"]
