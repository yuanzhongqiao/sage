r"""
Affine Lie Conformal Algebra

The affine Kac-Moody Lie conformal algebra associated to the
finite dimensional simple Lie algebra `\mathfrak{g}`. For a commutative
ring `R`, it is the `R[T]`-module freely generated by `\mathfrak{g}`
plus a central element `K` satisfying `TK = 0`. The non-vanishing
`\lambda`-brackets are given by

.. MATH::

    [a_\lambda b] = [a,b] + \lambda (a,b)K,

where `a,b \in \mathfrak{g}` and `(a,b)` is the normalized
form of `\mathfrak{g}` so that its longest root has square-norm
`2`.

AUTHORS:

- Reimundo Heluani (2019-08-09): Initial implementation.
"""

#******************************************************************************
#       Copyright (C) 2019 Reimundo Heluani <heluani@potuz.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#                  http://www.gnu.org/licenses/
#*****************************************************************************

from sage.rings.integer import Integer
from sage.algebras.lie_algebras.lie_algebra import LieAlgebra
from .graded_lie_conformal_algebra import GradedLieConformalAlgebra

class AffineLieConformalAlgebra(GradedLieConformalAlgebra):
    r"""
    The current or affine Kac-Moody Lie conformal algebra.

    INPUT:

    - ``R`` -- a commutative Ring; the base ring for this Lie
      conformal algebra.
    - ``ct`` -- a ``str`` or a :mod:`CartanType<sage.combinat.\
      root_system.cartan_type>`; the Cartan Type for
      the corresponding finite dimensional Lie algebra. It must
      correspond to a simple finite dimensional Lie algebra.
    - ``names`` -- a list of ``str`` or ``None`` (default: ``None``)
      ; alternative names for the generators. If ``None`` the
      generators are labeled by the corresponding root and coroot
      vectors.
    - ``prefix`` -- a ``str``; parameter passed to
      :class:`IndexedGenerators<sage.structure.indexed_generators.IndexedGenerators>`
    - ``bracket`` -- a ``str``; parameter passed to
      :class:`IndexedGenerators<sage.structure.indexed_generators.IndexedGenerators>`.

    EXAMPLES::

        sage: R = lie_conformal_algebras.Affine(QQ, 'A1')
        sage: R
        The affine Lie conformal algebra of type ['A', 1] over Rational Field
        sage: R.an_element()
        B[alpha[1]] + B[alphacheck[1]] + B[-alpha[1]] + B['K']

        sage: R = lie_conformal_algebras.Affine(QQ, 'A1', names = ('e', 'h','f'))
        sage: R.inject_variables()
        Defining e, h, f, K
        sage: Family(e.bracket(f.T(3)))
        Finite family {0: 6*T^(3)h, 1: 6*T^(2)h, 2: 6*Th, 3: 6*h, 4: 24*K}

        sage: V = lie_conformal_algebras.Affine(QQ, CartanType(["A",2,1]))
        Traceback (most recent call last):
        ...
        ValueError: only affine algebras of simple finite dimensionalLie algebras are implemented

    OUTPUT:

    The Affine Lie conformal algebra associated with the finite
    dimensional simple Lie algebra of Cartan type ``ct``.
    """
    def __init__(self, R, ct, names=None, prefix=None, bracket=None):
        """
        Initialize self.

        TESTS::

            sage: V = lie_conformal_algebras.Affine(QQ,'A1')
            sage: TestSuite(V).run()
        """
        if type(ct) is str:
            from sage.combinat.root_system.cartan_type import CartanType
            try:
                ct = CartanType(ct)
            except IndexError:
                raise ValueError("ct must be a valid Cartan Type")
        if not (ct.is_finite() and ct.is_irreducible ):
            raise ValueError("only affine algebras of simple finite dimensional"
                "Lie algebras are implemented")
        hv = Integer(ct.dual_coxeter_number())
        g = LieAlgebra(R, cartan_type=ct)
        B = g.basis()
        S = B.keys()
        gdict = {}
        for k1 in S:
            for k2 in S:
                if S.rank(k2) <= S.rank(k1):
                    myb = B[k1].bracket(B[k2]).monomial_coefficients()
                    myf = R(2).inverse_of_unit()*R(hv).inverse_of_unit()\
                          *g.killing_form(B[k1],B[k2])
                    if myb or myf:
                        gdict[(k1,k2)] = {}
                        if myb:
                            gdict[(k1,k2)][0] = {(nk,0):v for nk,v in \
                                                                    myb.items()}
                        if myf:
                            gdict[(k1,k2)][1] = {('K',0):myf}

        weights = (1,)*B.cardinality()
        self._ct = ct
        if prefix is None and names is None:
            prefix = 'B'

        GradedLieConformalAlgebra.__init__(self,
                    R, gdict, index_set=S,
                    central_elements=('K',), weights=weights,
                    names=names, prefix=prefix,bracket=bracket)

    def cartan_type(self):
        """
        The Cartan type of this Lie conformal algbera.

        EXAMPLES::

            sage: R = lie_conformal_algebras.Affine(QQ, 'B3')
            sage: R
            The affine Lie conformal algebra of type ['B', 3] over Rational Field
            sage: R.cartan_type()
            ['B', 3]
        """
        return self._ct

    def _repr_(self):
        """
        The name of this Lie conformal algebra.

        EXAMPLES::

            sage: lie_conformal_algebras.Affine(QQ, 'A1')
            The affine Lie conformal algebra of type ['A', 1] over Rational Field
        """
        return "The affine Lie conformal algebra of type {} over {}".format(
                                                    self._ct,self.base_ring())