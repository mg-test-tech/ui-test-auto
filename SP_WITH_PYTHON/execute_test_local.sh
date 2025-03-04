#!/bin/bash

pwd
cd ./data
pwd
rm ./results/*
cd ..
pwd
behave -f allure_behave.formatter:AllureFormatter -o ./data/results/ ./features/SP_assessment.feature
./local_execs/allure-2.13.1/bin/allure generate --clean ./data/results