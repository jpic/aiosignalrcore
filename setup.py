import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="signalrcore",
    version="0.8.0",
    author="mandrewcito",
    author_email="anbaalo@gmail.com",
    description="A Python SignalR Core client, with invocation auth and two way streamming. Also automatic reconnect and manually reconnect ",
    keywords="signalr core client 3.0",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mandrewcito/signalrcore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        "requests>=2.21.0",
        "websocket-client>=0.55.0"
    ]
)
