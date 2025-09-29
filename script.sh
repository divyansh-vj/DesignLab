# set variables
APP_ID=2033097
APP_NAME="MyApp-divyansh-vj"
OWNER="divyansh-vj"
REPO="DesignLab"
INSTALLATION_TOKEN=$GH_TOKEN

# set git identity to app
git config user.name "${APP_NAME}[bot]"
git config user.email "${APP_ID}+${APP_NAME}[bot]@users.noreply.github.com"

# create branch, commit
git checkout -b apps/test-bypass-branch
# edit files...
git add .
git commit -m "test: ruleset bypass"

# push using installation token
git remote set-url origin "https://x-access-token:${INSTALLATION_TOKEN}@github.com/${OWNER}/${REPO}.git"
git push -u origin apps/test-bypass-branch

# create PR as the app (installation token)
curl -s -X POST -H "Authorization: token ${INSTALLATION_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/repos/${OWNER}/${REPO}/pulls" \
  -d '{"title":"Test ruleset bypass","head":"apps/test-bypass-branch","base":"main","body":"testing bypass"}' | jq -r '.html_url'

