import time

from psychopy import core, visual, gui, data, event, logging
from psychopy.tools.filetools import fromFile, toFile
from psychopy.hardware import keyboard
from random import shuffle, random, randint, choice
import matplotlib
import matplotlib.pyplot as plt
import os

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

try:  # try to get a previous parameters file
    expInfo = fromFile('lastParams.pickle')
except:  # if not there then use a default set
    # Store info about the experiment session
    expName = 'DNMS-DMS'  # from the Builder filename that created this script
    expInfo = {'participant': '', 'session': '001', 'date': data.getDateStr(), 'expName': expName}
dlg = gui.DlgFromDict(expInfo, title='DNMS/DMS', fixed=['dateStr'])
if dlg.OK:
    toFile('lastParams.pickle', expInfo)  # save params to file for next time
else:
    core.quit()  # the user hit cancel so exit

# make a text file to save data
fileName = expInfo['participant'] + '_' + expInfo['date']
dataFile = open('DNMS/DNMScsv/' + fileName + '.csv', 'w')  # a simple text file with 'comma-separated-values'
dataFile.write('no_trial, id_candidate, id_first_im, id_second_im, good_ans, ans_candidate, keyboard_pressed, '
               'correct, task, practice, reaction_time, time_stamp\n')

filename = _thisDir + os.sep + u'DNMS/DNMSlog/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# save a log file for detail verbose info
logFile = logging.LogFile(filename + '.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


class DNMS:
    # create init w/ users data
    def __init__(self, start):
        self.start = start
        self.keys = ['a', 'p']
        self.colors = 'red yellow'.split()
        self.cmap = matplotlib.colors.ListedColormap(self.colors, name='colors', N=None)
        # self.list_cmaps = list()

    def run(self):
        pics = [pic for pic in range(100)]
        dict_cmap = {0: 20, 1: 20, 2: 20, 3: 20, 4: 20}
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0, allowStencil=False,
            monitor='testMonitor', color='black', colorSpace='rgb', useFBO=True,
            units='height')
        win.mouseVisible = False
        instr = visual.TextStim(win=win, name='instr',
                                text="Bonne chance !",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()
        core.wait(2)

        for i in range(8):
            if i == 0 or i == 4:
                self.practice(win, i)
            name_list = []
            rnd = randint(0, 4)
            while dict_cmap[rnd] == 0:
                rnd = randint(0, 4)
            dict_cmap[rnd] -= 1
            bgmain = visual.ImageStim(
                win=win, name='bgMain', units='height',
                image='cmap/cmap_' + str(rnd) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))
            bgmain.draw(win)
            win.flip()
            core.wait(0.7)
            win.flip()
            fixation_cross = visual.TextStim(win=win, name='fix_cr',
                                             text="+",
                                             font='Arial',
                                             units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                             color='white', colorSpace='rgb', opacity=1,
                                             languageStyle='LTR',
                                             depth=0.0)
            fixation_cross.draw()
            win.flip()
            core.wait(2)
            win.flip()
            choice_pos = randint(0, 1)
            c = choice(pics)
            pics.remove(c)
            name_list.extend((str(rnd), str(c)))
            if i < 4:
                task = 'DNMS'
                if choice_pos == 0:
                    good_ans = 'a'
                else:
                    good_ans = 'p'
            else:
                task = 'DMS'
                if choice_pos == 0:
                    good_ans = 'p'
                else:
                    good_ans = 'a'

            targ_0 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='cmap/cmap_' + str(rnd) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))
            targ_1 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='batch/test_cmap_' + str(c) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            if choice_pos == 0:
                targ_0.draw()
                win.flip()
                core.wait(0.7)
                targ_1.draw()
                win.flip()
                core.wait(0.7)
                win.flip()
            else:
                targ_1.draw()
                win.flip()
                core.wait(0.7)
                targ_0.draw()
                win.flip()
                core.wait(0.7)
                win.flip()
            resp, rt = self.get_response()
            if resp == good_ans:
                correct = True
                im_choose = c
                instr = visual.TextStim(win=win, name='instr',
                                        text="Bon !",
                                        font='Arial',
                                        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                        color='green', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=0.0)
                instr.draw()
                win.flip()
            else:
                correct = False
                im_choose = rnd
                instr = visual.TextStim(win=win, name='instr',
                                        text="Faux",
                                        font='Arial',
                                        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                        color='red', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=0.0)
                instr.draw()
                win.flip()
            dataFile.write(str(i) + ',' + expInfo['participant'] + ',' + str(name_list[0]) + ',' + str(name_list[1])
                           + ',' + str(c) + ',' + str(im_choose) + ',' + str(good_ans) + ',' + str(correct) + ',' +
                           str(task) + ',' + 'no' + ',' + str(round(rt, 2)) + ',' + str(round(time.time() - start, 2))
                           + '\n')
            core.wait(2)
            break_DNMS = visual.TextStim(win=win, name='instr',
                                         text="Merci ! \n Faisons une pause de 5 minutes avant de passer à la tâche "
                                              "suivante. \n",
                                         font='Arial',
                                         units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                         color='white', colorSpace='rgb', opacity=1,
                                         languageStyle='LTR',
                                         depth=0.0)
            if i == 3:
                break_DNMS.draw()
                win.flip()
                core.wait(10)
        thanks = visual.TextStim(win=win, name='thanks',
                                 text="Merci ! \n Bonne journée \n",
                                 font='Arial',
                                 units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                                 color='white', colorSpace='rgb', opacity=1,
                                 languageStyle='LTR',
                                 depth=0.0)
        thanks.draw()
        win.flip()
        core.wait(2)
        DNMS.quit_experiment(self)

    def practice(self, win, i):
        # start of instructions
        cpt = 0
        instr = visual.TextStim(win=win, name='instr',
                                text="Dans ce mini-jeu, vous devez choisir à l’aide des flèches le côté où le schéma "
                                     "affiché est différent du premier schéma.\n Puisqu’une image vaut mieux que "
                                     "mille mots, commençons par un petit entraînement ! \n Appuyez sur  ‘espace’ dès "
                                     "que vous êtes prêts.",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()
        resp = event.waitKeys(keyList=['space'])
        instr = visual.TextStim(win=win, name='instr',
                                text="Bienvenue dans l'entraînement !",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()

        for j in range(3):
            name_list_prac = []
            core.wait(2)
            bgmain = visual.ImageStim(
                win=win, name='bgMain', units='height',
                image='practice/pract_cmap_' + str(j) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))
            bgmain.draw(win)
            win.flip()
            core.wait(0.7)
            win.flip()
            fixation_cross = visual.TextStim(win=win, name='fix_cr',
                                             text="+",
                                             font='Arial',
                                             units='height', pos=(0, 0), height=0.2, wrapWidth=None, ori=0,
                                             color='white', colorSpace='rgb', opacity=1,
                                             languageStyle='LTR',
                                             depth=0.0)
            fixation_cross.draw()
            win.flip()
            core.wait(2)
            win.flip()
            choice_pos = randint(0, 1)
            pics = [pic for pic in range(2)]
            c = choice(pics)
            pics.remove(c)
            name_list_prac.extend((str(i), str(c)))
            if i == 0:
                task = 'DNMS'
                if choice_pos == 0:
                    good_ans = 'a'
                else:
                    good_ans = 'p'
            elif i == 4:
                task = 'DMS'
                if choice_pos == 0:
                    good_ans = 'p'
                else:
                    good_ans = 'a'

            targ_0 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='practice/pract_cmap_' + str(j) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            targ_1 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='practice/test_cmap_' + str(c) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            if choice_pos == 0:
                targ_0.draw()
                win.flip()
                core.wait(0.7)
                targ_1.draw()
                win.flip()
                core.wait(0.7)
                win.flip()
            else:
                targ_1.draw()
                win.flip()
                core.wait(0.7)
                targ_0.draw()
                win.flip()
                core.wait(0.7)
                win.flip()

            resp, rt = self.get_response()
            if resp == good_ans:
                cpt += 1
                correct = True
                im_chosen = c
                instr = visual.TextStim(win=win, name='instr',
                                        text="Bonne réponse !",
                                        font='Arial',
                                        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                        color='green', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=0.0)
                instr.draw()
                win.flip()
            else:
                correct = False
                im_chosen = j
                instr = visual.TextStim(win=win, name='instr',
                                        text="Faux ! \n (Rappel : il faut choisir le schéma différent de celui montré "
                                             "en premier lieu ! \n Prenez votre temps si nécessaire :) ) \n",
                                        font='Arial',
                                        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                        color='red', colorSpace='rgb', opacity=1,
                                        languageStyle='LTR',
                                        depth=0.0)
                instr.draw()
                win.flip()

            dataFile.write(
                str(j) + ',' + expInfo['participant'] + ',' + str(name_list_prac[0]) + ',' + str(name_list_prac[1]) +
                ',' + str(c) + ',' + str(im_chosen) + ',' + str(good_ans) + ',' + str(correct) + ',' + task + ', oui'
                + ',' + str(round(rt, 2)) + ',' + str(round(time.time() - start, 2)) + '\n')

        core.wait(4.0)
        if cpt == 3 or cpt == 2:
            instr = visual.TextStim(win=win, name='instr',
                                    text="Bravo, vous avez marqué " + str(cpt) + " points sur 3 ! \n Taux de réussite "
                                                                                 ": " + str(
                                        round(cpt * 100 / 3, 2)) + " % \n",
                                    font='Arial',
                                    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                    color='white', colorSpace='rgb', opacity=1,
                                    languageStyle='LTR',
                                    depth=0.0)
            instr.draw()
            win.flip()
        elif cpt == 0 or cpt == 1:
            instr = visual.TextStim(win=win, name='instr',
                                    text="Vous avez marqué " + str(
                                        cpt) + " points sur 3, mais vous avez à présent compris le principe !  \n",
                                    font='Arial',
                                    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                    color='white', colorSpace='rgb', opacity=1,
                                    languageStyle='LTR',
                                    depth=0.0)
            instr.draw()
            win.flip()
        core.wait(2)
        instr = visual.TextStim(win=win, name='instr',
                                text="Fin de l'entraînement. \n Passons à la tâche cognitive ! \n",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()
        core.wait(5)

    # ----------------------------------------------------------------------------------------------------

    def pause(self):
        # after 15 experiments, break of 10 seconds
        core.wait(15)

    def quit_experiment(self):
        exit()

    def get_response(self):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        rt_timer = core.MonotonicClock()
        keys = self.keys + ['q']
        resp = event.waitKeys(keyList=keys, timeStamped=rt_timer)

        if 'q' in resp[0]:
            self.quit_experiment()
        return resp[0][0], resp[0][1] * 1000  # key and rt in milliseconds

    def all_cmaps(self, matrix, n_cols):
        colors = 'red yellow'.split()
        cmap = matplotlib.colors.ListedColormap(colors, name='colors', N=None)
        plt.figure(figsize=(n_cols * 1.4, 1.6))
        for col in range(n_cols):
            plt.subplot(1, n_cols, col + 1)
            plt.imshow(self.gen_matrix(), cmap=cmap)
            plt.axis('off')
            plt.title('cmap_' + str(col))
        plt.show()

    @staticmethod
    def gen_matrix():
        random_m = [[randint(0, 1) for _ in range(4)] for _ in range(4)]
        return random_m

    def save_cmaps(self):
        for num in range(100):
            mat = DNMS.gen_matrix()
            plt.imshow(mat, cmap=self.cmap)
            plt.axis('off')
            plt.savefig(r'batch/test_cmap_' + str(num) + '.png')


start = time.time()
exp = DNMS(start)
exp.run()
