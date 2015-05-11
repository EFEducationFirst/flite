#!/bin/bash
ORIGDIR=`pwd`
TMPDIR=flite.$$

mkdir -p ../${TMPDIR}

cd ..
cp -a libflite ${TMPDIR}/flite-2.0.0
cd ${TMPDIR}
rm -rf flite-2.0.0/.git*
tar zcvf flite-2.0.0.tar.gz flite-2.0.0
mv flite-2.0.0.tar.gz ${ORIGDIR}/.
cd ${ORIGDIR}
rm -rf ../${TMPDIR}
