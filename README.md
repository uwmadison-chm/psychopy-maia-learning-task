# Reinforcement Learning task

Task originally described in [Harrison et al. (2016) A Neurocomputational Account of How Inflammation Enhances Sensitivity to Punishments Versus Rewards.](https://dx.doi.org/10.1016%2Fj.biopsych.2015.07.018).

Psychopy Builder version of task ported from original Matlab by Dan Fitch <dfitch@wisc.edu>.

# Features

* Psuedorandom seeding based on participant and session number

# TODO

* Button box? Go/no go and feedback changes? (Display circle at keypress? "The choice was then circled in red and the outcome displayed on the screen after a 4-second delay.")
* Sim version?
* Analysis: Do we need to worry about the Bayesian stuff, or the reinforcement-learning model they did? They provided no analysis code to us.
* Multiple sessions, do we try to prevent overlap of symbols? Sim is separate stimuli pool... We have 24 total stimuli.
* What about Kannadigas or people who can read the script? There's 44 million native speakers...

## Differences from original task

* BUGFIX: Runs of non-default length still use intended 80% predictability,
instead of skewing more toward completely random the shorter the trials
and toward 100% the longer the session goes. (In the shorter simulation runs, 
the Matlab task is more random than intended.)

## Credits

* [Dollar bill photo by NeONBRAND](https://unsplash.com/photos/8fDhgAN5zG0) on Unsplash.


## Original task implementation comments

Participant's goal is to maximise gains and minimise losses by choosing
the appropriate image from a presented pair of images. Participant has no
prior knowledge of which images correspond to which output.
Each pair of images corresponds to either a "gain", "look" (neutral) or
"lose" response, with one of each pair assigned to that response,
displaying the word and image of a coin and the other to display
"nothing" with no image of a coin. 
Approx 20% of the time however, the result assigned to each image in the
pair is reversed.

In current state, scanner pulses five times with the task starting on the
sixth pulse

Participant PRESSES BUTTON to chose RIGHT IMAGE, otherwise left
is selected. Participant cannot change response when button pressed.

Images associated with each response are randomised using clock-time as
the seed each session.

Images must change between sessions to ensure participant does not try to
use knowledge of image responses from previous session. For BIODEP, this
is already enforced in the two different codes, 'PC' and 'scanner'.


# License

This code is copyright 2019 the UW-Madison Board of Regents, and released under the MIT license.
