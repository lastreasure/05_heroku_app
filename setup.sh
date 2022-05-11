#!/bin/bash
export DATABASE_URL="postgresql://postgres@localhost:5432/postgres"
# export DATABASE_URL="postgres://grfglsulytfzja:14c91397a1fe94ec54d4c6b7c19b93b566eb00a67c7153a9b7ccc6e1abf48017@ec2-52-4-104-184.compute-1.amazonaws.com:5432/d5ccq30dqbfn7"
export EXCITED="true"
export AUTH0_DOMAIN="dev-yl9akfdv.us.auth0.com"
export API_AUDIENCE="casting"
export CLIENT_ID="h1BDlbmofIu7EMYKcTEbtCn6Xgsbeirj"
export REDIRECT_URI="https://nano-proj5.herokuapp.com/"
export ALGORITHMS=['RS256']
echo "setup.sh script executed successfully!"