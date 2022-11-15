#!/usr/bin/env bash
mkdir -p .dagster
export DAGSTER_HOME=`pwd`/.dagster
exec dagster-daemon run -w app/workspace.yaml $@
