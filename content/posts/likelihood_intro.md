Title: Practical Bayesian statistics
Date: 2024-07-03
Category: Post
Tags: Statistics, Data
Author: Ata Sattari
Summary: A brief review of Bayesian statistics, computational challenges, and numerical algorithms.

## Bayesian statistics, computational challenges, and numerical methods

Physics measurements rely on two key components. The first is a theoretical model that predicts the experimental outcome, and the second is the data collected from an experimental apparatus. The model typically involves a set of unknown parameters, which are divided into two categories: those related to fundamental physical properties and those tied to the experimental apparatus. For example, the mass of an electron falls into the first category, while the precision of the device measuring the mass belongs to the second. The primary goal of an experiment is to determine the values of these unknown parameters, with a particular focus on those linked to fundamental physics. A common approach to achieve this is by combining the data with the theoretical model to construct a likelihood function. At the name suggests, this function quantifies the likelihood of observing the data given the model. This note provides a basic introduction to the likelihood framework from the perspective of an **astroparticle physicist** and a **statistics practitioner**.

Imagine tossing beads at a stationary target (the measuring device). After each impact, the device records the energy deposited, which can be thought of as small vibrations. This process is repeated to collect a dataset of energy values. An example dataset is shown below:

<center>   <img src="{static}pictures/image.png" alt="Distribution according to a Gaussian function" width="500"> </center>

The goal is to ultimately determine the average energy deposited by the beads. For simplicity, we assume that the energy deposited by each bead is nearly identical; however, the measuring device reports these energies with some level of error (uncertainty).




A computational challenge in evaluating the posterior probability distribution function (PDF) following
\begin{equation}         
     \text{Posterior}(\theta|\text{data}) = \frac{L(\text{data}|\theta) \cdot \pi(\theta)}{\text{Evidence}},
\end{equation}
is calculating the Evidence in the denominator. The Evidence is the integral of numerator over the entire parameter space of the floating parameters
\begin{equation}
     \int d\theta L(\text{data}|\theta) \cdot \pi(\theta),
\end{equation}
which normalizes the posterior function. Directly computing this high-dimensional integral by discretizing the parameter space becomes impractical very quickly. For instance, if each dimension is divided into 100 points and the parameter space spans 5 dimensions, the total number of points would be $100^5$. This exponential increase in computational complexity, often termed the 'curse of dimensionality,' makes calculating the Evidence infeasible as the number of unknown parameters grows.

asdasdasdasda

