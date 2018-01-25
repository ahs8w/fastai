from .learner import *

class Learner(Learner):
    def plot_loss_change(sched, sma=1, n_skip=20, y_lim=(-0.01,0.01)):
        """
        Plots rate of change of the loss function.
        Parameters:
            sched - learning rate scheduler, an instance of LR_Finder class.
            sma - number of batches for simple moving average to smooth out the curve.
            n_skip - number of batches to skip on the left.
            y_lim - limits for the y axis.

        Example:
            plot_loss_change(learn.sched, sma=20, y_lim=(-0.1, 0.01))
        """
        derivatives = [0] * (sma + 1)
        for i in range(1 + sma, len(learn.sched.lrs)):
            derivative = (learn.sched.losses[i] - learn.sched.losses[i - sma]) / sma
            derivatives.append(derivative)
            
        plt.ylabel("d/loss")
        plt.xlabel("learning rate (log scale)")
        plt.plot(learn.sched.lrs[n_skip:], derivatives[n_skip:])
        plt.xscale('log')
        plt.ylim(y_lim)