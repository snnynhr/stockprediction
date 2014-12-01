package edu.cmu.cs.ark.sage.effects;

import edu.cmu.cs.ark.sage.SAGE;

/**
 * This class is used to denote a {@link SAGE} effect.
 * <p>
 * You can inherit this class and add whatever meta data you like to it.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class Effect implements Comparable<Effect>
{
  private final boolean fixed;
  private double l1regularizer, l2regularizer;

  /**
   * Defaults to fixed effect with 0 regularization.
   */
  public Effect()
  {
    fixed = true;
    l1regularizer = 0.0;
    l2regularizer = 0.0;
  }

  /**
   * Constructs a non-fixed {@link Effect} with L1 regularization.
   * 
   * @param l1regularizer
   *          L1 regularization weight.
   */
  public Effect(double l1regularizer)
  {
    this.fixed = false;
    this.l1regularizer = l1regularizer;
  }

  /**
   * Constructs a non-fixed {@link Effect} with L1 regularization and L2 regularization.
   * 
   * @param l1regularizer
   *          L1 regularization weight.
   * @param l2regularizer
   *          L2 regularization weight.
   */
  public Effect(double l1regularizer, double l2regularizer)
  {
    this.fixed = false;
    this.l1regularizer = l1regularizer;
    this.l2regularizer = l2regularizer;
  }

  /**
   * Returns if this is a fixed {@link Effect}.
   * 
   * @return <code>true</code> if this is a fixed {@link Effect}.
   */
  public boolean isFixed()
  {
    return fixed;
  }

  /**
   * Returns the L1 regularization weight of this effect.
   * 
   * @return the L1 regularization weight of this effect.
   */
  public double getL1Regularizer()
  {
    return l1regularizer;
  }

  /**
   * Sets the L1 regularization weight of this effect.
   * 
   * @param l1regularizer
   *          the L1 regularization weight of this effect.
   */
  public void setL1Regularizer(double l1regularizer)
  {
    this.l1regularizer = l1regularizer;
  }

  /**
   * Returns the L2 regularization weight of this effect.
   * 
   * @return the L2 regularization weight of this effect.
   */
  public double getL2Regularizer()
  {
    return this.l2regularizer;
  }

  /**
   * Sets the L2 regularization weight of this effect.
   * 
   * @param l2regularizer
   *          the L2 regularization weight of this effect.
   */
  public void setL2Regularizer(double l2regularizer)
  {
    this.l2regularizer = l2regularizer;
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString()
  {
    if (isFixed())
      return String.format("FixedEffect[%s]", getDescription());

    if (getL1Regularizer() > 0 && getL2Regularizer() > 0)
      return String.format("Effect[%s,L1=%f,L2=%f]", getDescription(), getL1Regularizer(), getL2Regularizer());
    if (getL1Regularizer() > 0)
      return String.format("Effect[%s,L1=%f]", getDescription(), getL1Regularizer());

    return String.format("Effect[%s,L2=%f]", getDescription(), getL2Regularizer());
  }

  /**
   * Returns the description of this effect (without extra information like regularization weight as that of {@link #toString()}).
   * 
   * @return the description of this effect
   */
  public String getDescription()
  {
    return "0x" + Integer.toHexString(hashCode());
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Comparable#compareTo(java.lang.Object)
   */
  @Override
  public int compareTo(Effect o)
  {
    return getDescription().compareTo(o.getDescription());
  }
}
