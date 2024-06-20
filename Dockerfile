FROM ghcr.io/prefix-dev/pixi:latest AS build

COPY . /app
WORKDIR /app
RUN pixi run build
RUN pixi run install-dist
RUN pixi shell-hook -e prod > /shell-hook
RUN echo "uvicorn orcestrator.main:app --host 0.0.0.0 --port 8000 --reload" >> /shell-hook

FROM ubuntu:22.04 AS production

# only copy the production env and the shell-hook script to the production image
WORKDIR /app
COPY --from=build /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --from=build /shell-hook /shell-hook


EXPOSE 8000
CMD ["/bin/bash", "/shell-hook"]
