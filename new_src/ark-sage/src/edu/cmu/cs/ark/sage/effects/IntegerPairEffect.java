package edu.cmu.cs.ark.sage.effects;

/**
 * This is an implementation of a SAGE {@link Effect} that is indexed by a pair of <code>int</code>s.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class IntegerPairEffect extends Effect
{
  private final int a, b;

  /**
   * Construct a fixed {@link IntegerPairEffect} object with <code>id a</code> and <code>b</code>.
   * 
   * @param a
   * @param b
   *          the <code>id</code>s of this effect.
   */
  public IntegerPairEffect(int a, int b)
  {
    super();
    this.a = a;
    this.b = b;
  }

  /**
   * Construct a non-fixed {@link IntegerPairEffect} object with <code>id a</code> and <code>b</code> and L1 regularization.
   * 
   * @param a
   * @param b
   *          the <code>id</code>s of this effect.
   * @param l1regularizer
   *          L1 regularization weight.
   */
  public IntegerPairEffect(int a, int b, double l1regularizer)
  {
    super(l1regularizer);
    this.a = a;
    this.b = b;
  }

  /**
   * Construct a non-fixed {@link IntegerPairEffect} object with <code>id a</code> and <code>b</code> and L1/L2 regularization.
   * 
   * @param a
   * @param b
   *          the <code>id</code>s of this effect.
   * @param l1regularizer
   *          L1 regularization weight.
   * @param l2regularizer
   *          L2 regularization weight.
   */
  public IntegerPairEffect(int a, int b, double l1regularizer, double l2regularizer)
  {
    super(l1regularizer, l2regularizer);
    this.a = a;
    this.b = b;
  }

  @Override
  public String getDescription()
  {
    return String.format("%d,%d", a, b);
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#hashCode()
   */
  @Override
  public int hashCode()
  {
    return 961 + (31 * a) + b;
  }

  /**
   * Tests for equality by comparing the <code>id</code> pair of two {@link IntegerPairEffect}s.
   * 
   * @see java.lang.Object#equals(java.lang.Object)
   */
  @Override
  public boolean equals(Object obj)
  {
    if (this == obj)
      return true;
    if (obj == null || getClass() != obj.getClass())
      return false;

    IntegerPairEffect other = (IntegerPairEffect) obj;
    if (a != other.a || b != other.b)
      return false;
    return true;
  }
}
