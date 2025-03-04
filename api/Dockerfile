FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS development

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY pyproject.toml ./

RUN uv sync

COPY . /app


FROM development AS prod

COPY --from=development /app /app

RUN uv sync --no-dev

EXPOSE 8000
CMD ["uv", "run", "main.py"]
