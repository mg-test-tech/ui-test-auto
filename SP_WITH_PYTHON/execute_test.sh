#!/bin/bash

pwd
cd ./SP_WITH_PYTHON/data
pwd
rm ./SP_WITH_PYTHON/results/*
cd ..
pwd
behave -f allure_behave.formatter:AllureFormatter -o ./SP_WITH_PYTHON/data/results/ ./SP_WITH_PYTHON/features/SP_assessment.feature
./local_execs/allure-2.13.1/bin/allure generate --clean ./SP_WITH_PYTHON/data/results