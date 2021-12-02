import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	try:
		ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	except Exception, e:
		print("Could not create a proxy to ALTextToSpeech")

	ttsProxy.say("HELLO")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.3, 0.933333, 1.5, 1.96667, 2.53333, 3.46667, 4])
	keys.append([[0.29602, [3, -0.1, 0], [3, 0.211111, 0]], [-0.170316, [3, -0.211111, 0.111996], [3, 0.188889, -0.100207]], [-0.340591, [3, -0.188889, 0], [3, 0.155556, 0]], [-0.0598679, [3, -0.155556, 0], [3, 0.188889, 0]], [-0.193327, [3, -0.188889, 0], [3, 0.311111, 0]], [-0.01078, [3, -0.311111, -0.0419879], [3, 0.177778, 0.0239931]], [0.0132131, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([0.3, 0.933333, 1.5, 1.96667, 2.53333, 3.46667, 4])
	keys.append([[-0.135034, [3, -0.1, 0], [3, 0.211111, 0]], [-0.351328, [3, -0.211111, 0.0493864], [3, 0.188889, -0.0441878]], [-0.415757, [3, -0.188889, 0.00372364], [3, 0.155556, -0.00306653]], [-0.418823, [3, -0.155556, 0.00306653], [3, 0.188889, -0.00372364]], [-0.520068, [3, -0.188889, 0], [3, 0.311111, 0]], [-0.375872, [3, -0.311111, -0.109175], [3, 0.177778, 0.0623858]], [-0.00538521, [3, -0.177778, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([0.233333, 0.866667, 1.43333, 1.9, 2.46667, 3.4, 4])
	keys.append([[-1.37902, [3, -0.0777778, 0], [3, 0.211111, 0]], [-1.29005, [3, -0.211111, -0.0345436], [3, 0.188889, 0.0309074]], [-1.18267, [3, -0.188889, 0], [3, 0.155556, 0]], [-1.24863, [3, -0.155556, 0.0205524], [3, 0.188889, -0.0249565]], [-1.3192, [3, -0.188889, 0], [3, 0.311111, 0]], [-1.18421, [3, -0.311111, -0.0631762], [3, 0.2, 0.0406133]], [-1.00783, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.233333, 0.866667, 1.43333, 1.9, 2.46667, 3.4, 4])
	keys.append([[-0.803859, [3, -0.0777778, 0], [3, 0.211111, 0]], [-0.691876, [3, -0.211111, -0.0137171], [3, 0.188889, 0.0122732]], [-0.679603, [3, -0.188889, -0.0122732], [3, 0.155556, 0.0101073]], [-0.610574, [3, -0.155556, 0], [3, 0.188889, 0]], [-0.753235, [3, -0.188889, 0], [3, 0.311111, 0]], [-0.6704, [3, -0.311111, 0], [3, 0.2, 0]], [-1.37846, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.866667, 3.4, 4])
	keys.append([[0.238207, [3, -0.288889, 0], [3, 0.844444, 0]], [0.240025, [3, -0.844444, -0.001818], [3, 0.2, 0.000430579]], [0.247252, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.233333, 0.866667, 1.43333, 1.9, 2.46667, 3.4, 4])
	keys.append([[1.11824, [3, -0.0777778, 0], [3, 0.211111, 0]], [0.928028, [3, -0.211111, 0], [3, 0.188889, 0]], [0.9403, [3, -0.188889, 0], [3, 0.155556, 0]], [0.862065, [3, -0.155556, 0], [3, 0.188889, 0]], [0.897349, [3, -0.188889, 0], [3, 0.311111, 0]], [0.842125, [3, -0.311111, 0], [3, 0.2, 0]], [1.38864, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.233333, 0.866667, 1.43333, 1.9, 2.46667, 3.4, 4])
	keys.append([[0.363515, [3, -0.0777778, 0], [3, 0.211111, 0]], [0.226991, [3, -0.211111, 0.0257175], [3, 0.188889, -0.0230104]], [0.20398, [3, -0.188889, 0], [3, 0.155556, 0]], [0.217786, [3, -0.155556, -0.00669692], [3, 0.188889, 0.00813198]], [0.248467, [3, -0.188889, 0], [3, 0.311111, 0]], [0.226991, [3, -0.311111, 0], [3, 0.2, 0]], [0.310039, [3, -0.2, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.866667, 3.4, 4])
	keys.append([[0.147222, [3, -0.288889, 0], [3, 0.844444, 0]], [0.11961, [3, -0.844444, 0.027612], [3, 0.2, -0.00653968]], [0.00831442, [3, -0.2, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.166667, 0.8, 1.03333, 1.36667, 1.63333, 1.83333, 2.16667, 2.4, 2.73333, 3.33333, 4])
	keys.append([[1.38524, [3, -0.0555556, 0], [3, 0.211111, 0]], [0.242414, [3, -0.211111, 0], [3, 0.0777778, 0]], [0.349066, [3, -0.0777778, -0.0949577], [3, 0.111111, 0.135654]], [0.934249, [3, -0.111111, 0], [3, 0.0888889, 0]], [0.680678, [3, -0.0888889, 0.141383], [3, 0.0666667, -0.106037]], [0.191986, [3, -0.0666667, 0], [3, 0.111111, 0]], [0.261799, [3, -0.111111, -0.0698132], [3, 0.0777778, 0.0488692]], [0.707216, [3, -0.0777778, -0.103967], [3, 0.111111, 0.148524]], [1.01927, [3, -0.111111, -0.0664734], [3, 0.2, 0.119652]], [1.26559, [3, -0.2, 0], [3, 0.222222, 0]], [0.995286, [3, -0.222222, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([0.166667, 0.8, 1.36667, 1.83333, 2.4, 2.73333, 3.33333, 4])
	keys.append([[-0.312978, [3, -0.0555556, 0], [3, 0.211111, 0]], [0.564471, [3, -0.211111, 0], [3, 0.188889, 0]], [0.391128, [3, -0.188889, 0.0395378], [3, 0.155556, -0.0325606]], [0.348176, [3, -0.155556, 0], [3, 0.188889, 0]], [0.381923, [3, -0.188889, -0.0337477], [3, 0.111111, 0.0198516]], [0.977384, [3, -0.111111, 0], [3, 0.2, 0]], [0.826783, [3, -0.2, 0], [3, 0.222222, 0]], [1.38305, [3, -0.222222, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.8, 2.4, 3.33333, 4])
	keys.append([[0.853478, [3, -0.266667, 0], [3, 0.533333, 0]], [0.854933, [3, -0.533333, 0], [3, 0.311111, 0]], [0.425116, [3, -0.311111, 0.119202], [3, 0.222222, -0.0851442]], [0.241895, [3, -0.222222, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.166667, 0.8, 1.36667, 1.83333, 2.4, 3.33333, 4])
	keys.append([[0.247016, [3, -0.0555556, 0], [3, 0.211111, 0]], [-1.17193, [3, -0.211111, 0], [3, 0.188889, 0]], [-1.0891, [3, -0.188889, 0], [3, 0.155556, 0]], [-1.26091, [3, -0.155556, 0], [3, 0.188889, 0]], [-1.14892, [3, -0.188889, -0.111982], [3, 0.311111, 0.184441]], [1.02015, [3, -0.311111, -0.492919], [3, 0.222222, 0.352085]], [1.38609, [3, -0.222222, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.166667, 0.8, 1.36667, 1.83333, 2.4, 3.33333, 4])
	keys.append([[-0.242414, [3, -0.0555556, 0], [3, 0.211111, 0]], [-0.954191, [3, -0.211111, 0], [3, 0.188889, 0]], [-0.460242, [3, -0.188889, 0], [3, 0.155556, 0]], [-0.960325, [3, -0.155556, 0], [3, 0.188889, 0]], [-0.328317, [3, -0.188889, -0.0474984], [3, 0.311111, 0.0782326]], [-0.250085, [3, -0.311111, 0], [3, 0.222222, 0]], [-0.292597, [3, -0.222222, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.8, 2.4, 3.33333, 4])
	keys.append([[-0.312978, [3, -0.266667, 0], [3, 0.533333, 0]], [-0.303775, [3, -0.533333, -0.00920312], [3, 0.311111, 0.00536849]], [0.182504, [3, -0.311111, 0], [3, 0.222222, 0]], [-0.0122155, [3, -0.222222, 0], [3, 0, 0]]])

	try:
		motion = ALProxy("ALMotion",robotIP,port)
		motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
		print err
  
  
if __name__ == "__main__":
	robotIP = "127.0.0.1"
	port = 9559

	if len(sys.argv) <= 1:
		print "(robotIP default: 127.0.0.1)"
	elif len(sys.argv) <= 2:
		robotIP = sys.argv[1]
	else:
		port = int(sys.argv[2])
		robotIP = sys.argv[1]

	start = time.time()
	main(robotIP, port)
	end = time.time()
	print ("%.2f seconds elapsed" % (end-start))