# Build pages
livemark build 000_livemark/index.md --target ./index.html --config 000_livemark/livemark.yaml && \
livemark build 001_setup/README.md --target 001_setup/README.html --config 000_livemark/livemark.yaml && \
livemark build 002_warm_up/001_terminal_101/README.md --target 002_warm_up/001_terminal_101/README.html --config 000_livemark/livemark.yaml && \
livemark build 002_warm_up/002_version_control_101/README.md --target 002_warm_up/002_version_control_101/README.html --config 000_livemark/livemark.yaml && \
livemark build 003_python_essentials/001_variables/README.md --target 003_python_essentials/001_variables/README.html --config 000_livemark/livemark.yaml && \
livemark build 003_python_essentials/002_strings/README.md --target 003_python_essentials/002_strings/README.html --config 000_livemark/livemark.yaml && \
livemark build 003_python_essentials/002_strings/LEIAME.md --target 003_python_essentials/002_strings/LEIAME.html --config 000_livemark/livemark.yaml && \

# Start server to test builded pages
livemark start 000_livemark/index.md --target ./index.html --config 000_livemark/livemark.yaml
