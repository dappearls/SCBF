if __name__ == "__main__":
	try:
		__import__("basari_enc").login_baz()
	except Exception as e:
		exit(str(e))
