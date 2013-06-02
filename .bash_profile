export PATH=/opt/local/bin:/opt/local/sbin:$HOME/local/node:$PATH

# Setting PATH for Python 2.7
# The orginal version is saved in .bash_profile.pysave
PATH="${PATH}:/Users/erikj/src/android-sdk-mac_x86/tools:/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/:/Library/Frameworks/Python.framework/Versions/2.7/bin:/tmp/my-android-toolchain/bin:/Developer/SDKs/bbndk-2.1.0-beta1/host/macosx/x86/usr/bin/"

#source "/Developer/SDKs/bbndk-2.1.0-beta1/bbndk-env.sh"
source "/Applications/bbndk/bbndk-env.sh"

export PATH

PYTHONPATH="/usr/local/lib/python2.7/site-packages:/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/:${PYTHONPATH}"

if [ $PYTHONPATH ]
then
    export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.6/:/usr/lib/python2.6/site-packages/
else
    export PYTHONPATH=/usr/lib/python2.6/:/usr/lib/python2.6/site-packages/
fi

#alias arm-gcc=/Users/erikj/Downloads/android-ndk-r7/toolchains/arm-linux-androideabi-4.4.3/prebuilt/darwin-x86/arm-linux-androideabi/bin/gcc

#[[ -s "/Users/erikj/.rvm/scripts/rvm" ]] && source "/Users/erikj/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*

export JAVA_HOME=/Library/Java/Home
export CATALINA_HOME=/Library/Tomcat/Home

