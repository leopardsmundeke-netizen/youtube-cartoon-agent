# Cartoon Doctor Studio — Automation

This repository is the GitHub-based automation core for the animated Ali + Dr. Sara health-comedy channel.

## Flow
Topic → Script → Safety Check → Voice Plan → Video Plan → Thumbnail Plan → SEO → Quality Check → YouTube upload plan.

## Important
The repository contains provider adapters, but external services still require valid API credentials and supported APIs. GitHub Actions cannot magically create an ElevenLabs voice, render a video, or upload to YouTube without those provider connections.

Keep all credentials in GitHub Actions Secrets; never commit keys to the repository.

Default publishing is private for testing. Change to public/scheduled only after a successful test.

## Local test
python src/run_episode.py

## GitHub Actions
The workflow can be run manually with a topic or on the configured schedule. It stores the generated episode JSON under episodes/.
