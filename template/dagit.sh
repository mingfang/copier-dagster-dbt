#!/usr/bin/env bash
mkdir -p .dagster
export DAGSTER_HOME=`pwd`/.dagster
exec dagit -h 0.0.0.0 -w app/workspace.yaml $@
