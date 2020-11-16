from DNMS import *

def quit_experiment(win):
    thanks = visual.TextStim(win=win, name='thanks',
                             text="Merci et bonne journée ! \n",
                             font='Arial',
                             units='height', pos=(0, 0), height=0.06, wrapWidth=None, ori=0,
                             color='white', colorSpace='rgb', opacity=1,
                             languageStyle='LTR',
                             depth=0.0)
    thanks.draw()
    win.flip()
    core.wait(2)
    core.quit()


class DMS:
    # create init w/ users data
    def __init__(self):
        self.keys = ['a', 'p']
        self.colors = 'red yellow'.split()
        self.cmap = matplotlib.colors.ListedColormap(self.colors, name='colors', N=None)
        # self.list_cmaps = list()

    def run(self):
        # endExpNow = False  # flag for 'escape' or other condition => quit the exp
        # start of instructions
        event.Mouse(visible=False)
        pics = [pic for pic in range(100)]
        dict_cmap = {0: 20, 1: 20, 2: 20, 3: 20, 4: 20}
        win = visual.Window(
            size=[1080, 800], fullscr=False, screen=0, allowStencil=False,
            monitor='testMonitor', color='black', colorSpace='rgb', useFBO=True,
            units='height')
        event.Mouse(visible=False)
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
        for i in range(100):
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
            core.wait(3.2)
            win.flip()
            choice_pos = randint(0, 1)
            # choose a pic
            c = choice(pics)
            pics.remove(c)
            name_list.append(str(rnd) + '/' + str(c))
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
                core.wait(1)
                fixation_cross.draw()
                win.flip()
                core.wait(2)
                targ_1.draw()
                win.flip()
                core.wait(1)
                win.flip()
            else:
                targ_1.draw()
                win.flip()
                core.wait(1)
                fixation_cross.draw()
                win.flip()
                core.wait(2)
                targ_0.draw()
                win.flip()
                core.wait(1)
                win.flip()
            resp, rt = self.get_response()
            if resp == good_ans:
                correct = True
                im_chosen = rnd
            else:
                correct = False
                im_chosen = c
            dataFile.write(str(i) + ',' + expInfo['participant'] + ',' + str(name_list[0]) + ',' + str(name_list[1]) +
                           ',' + str(c) + ',' + str(im_chosen) + ',' + str(good_ans) + ',' + str(correct) + ', DNMS, no'
                           + ',' + str(round(rt, 2)) + '\n')
            # on stock tout dans une liste
            core.wait(5)
        quit_experiment(win)

    def practice(self):
        # endExpNow = False  # flag for 'escape' or other condition => quit the exp
        # start of instructions
        cpt = 0
        event.Mouse(visible=False)
        win = visual.Window(
            size=[1920, 1080], fullscr=True, screen=0, allowStencil=False,
            monitor='testMonitor', color='black', colorSpace='rgb', useFBO=True,
            units='height')
        event.Mouse(visible=False)
        instr = visual.TextStim(win=win, name='instr',
                                text="Dans ce mini-jeu, vous devez choisir à l’aide des flèches le côté où le schéma "
                                     "affiché MMMMMMest le même que le premier schéma.\n Puisqu’une image vaut mieux que "
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

        for i in range(3):
            name_list_prac = []
            rnd_prac = randint(0, 4)
            core.wait(2)
            bgmain = visual.ImageStim(
                win=win, name='bgMain', units='height',
                image='practice/pract_cmap_' + str(i) + '.png', mask=None,
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
            core.wait(3.2)
            win.flip()
            choice_pos = randint(0, 1)
            pics = [pic for pic in range(2)]
            c = choice(pics)
            pics.remove(c)
            name_list_prac.extend((str(rnd_prac), str(c)))
            if choice_pos == 0:
                good_ans = 'p'
            else:
                good_ans = 'a'

            targ_0 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='practice/pract_cmap_' + str(rnd_prac) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            targ_1 = visual.ImageStim(
                win=win, name='targ', units='height',
                image='practice/test_cmap_' + str(c) + '.png', mask=None,
                ori=0, pos=(0, 0), size=(0.25, 0.25))

            if choice == 0:
                targ_0.draw()
                win.flip()
                core.wait(1)
                fixation_cross.draw()
                win.flip()
                core.wait(2)
                targ_1.draw()
                win.flip()
                core.wait(1)
                win.flip()
            else:
                targ_1.draw()
                win.flip()
                core.wait(1)
                fixation_cross.draw()
                win.flip()
                core.wait(2)
                targ_0.draw()
                win.flip()
                core.wait(1)
                win.flip()
            resp, rt = self.get_response()
            if resp == good_ans:
                cpt += 1
                correct = True
                im_chosen = rnd_prac
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
                im_chosen = c
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
                str(i) + ',' + expInfo['participant'] + ',' + str(name_list_prac[0]) + ',' + str(name_list_prac[1]) +
                ',' + str(c) + ',' + str(im_chosen) + ',' + str(good_ans) + ',' + str(correct) + ', DMS, no'
                + ',' + str(round(rt, 2)) + '\n')
        core.wait(4.0)
        if cpt == 3 or cpt == 2:
            instr = visual.TextStim(win=win, name='instr',
                                    text="Bravo, vous avez marqué " + str(cpt) + "points sur 3 ! \n Taux de réussite "
                                                                                 ": " + str(
                                        round(cpt * 100 / 3, 2)) + "% "
                                                                   "\n",
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
        core.wait(4)
        instr = visual.TextStim(win=win, name='instr',
                                text="Fin de l'entraînement. \n Passons aux choses sérieuses ! \n",
                                font='Arial',
                                units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
                                color='white', colorSpace='rgb', opacity=1,
                                languageStyle='LTR',
                                depth=0.0)
        instr.draw()
        win.flip()
        core.wait(5)

    # ----------------------------------------------------------------------------------------------------

    def get_response(self):
        """Waits for a response from the participant.
        Pressing Q while the function is wait for a response will quit the experiment.
        Returns the pressed key and the reaction time.
        """
        rt_timer = core.MonotonicClock()
        keys = self.keys + ['q']
        resp = event.waitKeys(keyList=keys, timeStamped=rt_timer)

        if 'q' in resp[0]:
            quit_experiment()
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
            mat = DMS.gen_matrix()
            plt.imshow(mat, cmap=self.cmap)
            plt.axis('off')
            plt.savefig(r'batch/test_cmap_' + str(num) + '.png')
