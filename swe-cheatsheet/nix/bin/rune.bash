export VERSION="3.7.1"
xcode-select --install
brew update
brew upgrade
brew install zlib
brew reinstall zlib
export LDFLAGS="-L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include"
pyenv install $VERSION
pyenv global $VERSION

