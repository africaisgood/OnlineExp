#!/usr/bin/env python
from planout.experiment import SimpleExperiment
from planout.ops.random import UniformChoice, WeightedChoice, Sample, RandomInteger

imgs = {
		'M1.jpg': 'M',
		'M2.jpg': 'M',
		'M3.jpg': 'M',
		'M4.jpg': 'M',
		'F1.jpg': 'F',
		'F2.jpg': 'F',
		'F3.jpg': 'F',
		'F4.jpg': 'F',}

#imgs = {('M%d.png'%((i//2)+1) if i%2==0 else 'F%d.png'%((i//2)+1)):('M' if i%2==0 else 'F') for i in xrange(8)} 

class BabyFaceExp(SimpleExperiment):

    def setup(self):
        pass
        # self.set_auto_exposure_logging(False)

    def assign(self, params, userid):
        params.cond = Sample(choices=imgs, unit=userid) #within


if __name__ == '__main__':

	for subj in xrange(2):
		exp = BabyFaceExp(userid=subj)
		print exp
		print