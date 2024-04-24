FROM ghcr.io/prefix-dev/pixi:latest AS build

COPY . /app
WORKDIR /app
RUN pixi run build-wheel
RUN pixi run install-dist
RUN pixi shell-hook -e prod > /shell-hook
RUN echo "python -m orcestrator.core.main" >> /shell-hook
FROM ubuntu:22.04 AS production

# only copy the production env and the shell-hook script to the production image
COPY --from=build /app/.pixi/envs/prod /app/.pixi/envs/prod
COPY --from=build /shell-hook /shell-hook

WORKDIR /app

SHELL ["/bin/bash", "-c"]

# ENTRYPOINT [ "/bin/bash", "/shell-hook" ]

ENTRYPOINT ["/bin/bash", "-c", "source /shell-hook && exec /bin/bash"]
