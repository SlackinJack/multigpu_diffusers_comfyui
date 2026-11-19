# starting on 07.27.2026, all requirements
# will be installed to the project dir's .venv


echo ""
echo "########## Clean Up Workspace ##########"
echo ""
rm -r .venv multigpu_diffusers
find -iname "__pycache__" | xargs rm -r


echo ""
echo "########## Clone multigpu_diffusers ##########"
echo ""
git clone https://github.com/slackinjack/multigpu_diffusers --depth=1


echo ""
echo "########## Setup multigpu_diffusers ##########"
echo ""
cd multigpu_diffusers
bash setup.sh
cd ..


echo ""
echo "########## Setup .venv ##########"
echo ""
cp multigpu_diffusers/requirements.txt req_multi.txt
cp multigpu_diffusers/AsyncDiff/requirements.txt req_async.txt
python3 -m venv .venv
source .venv/bin/activate && pip install --no-build-isolation -r req_async.txt
source .venv/bin/activate && pip install --no-build-isolation -r req_multi.txt
rm req_async.txt req_multi.txt


echo ""
echo "########## Setup node requirements ##########"
echo ""
pip install --no-build-isolation -r requirements.txt


echo ""
echo "########## Setup complete, enjoy! ##########"
echo ""
