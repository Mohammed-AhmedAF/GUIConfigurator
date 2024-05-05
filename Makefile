install_dep:
	pip3 install ttkbootstrap pyperclip pillow

uninstall_dep:
	pip3 uninstall -y ttkbootstrap pyperclip pillow

run: install_dep
	python3 ./uartconfigurator.py