package edu.cmu.cs.ark.sage.effects;

/**
 * This is an implementation of a SAGE {@link Effect} that is indexed by an <code>int</code> <code>id</code>.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class IntegerEffect extends Effect
{
  private final int id;

  /**
   * Construct a fixed {@link IntegerEffect} object with <code>id</code>.
   * 
   * @param id
   *          the <code>id</code> of this effect.
   */
  public IntegerEffect(int id)
  {
    super();
    this.id = id;
  }

  /**
   * Construct a non-fixed {@link IntegerEffect} object with <code>id</code> and L1 regularization.
   * 
   * @param id
   *          the <code>id</code> of this effect.
   * @param l1regularizer
   *          L1 regularization weight.
   */
  public IntegerEffect(int id, double l1regularizer)
  {
    super(l1regularizer);
    this.id = id;
  }

  /**
   * Construct a non-fixed {@link IntegerEffect} object with <code>id</code>, L1 and L2 regularization.
   * 
   * @param id
   *          the <code>id</code> of this effect.
   * @param l1regularizer
   *          L1 regularization weight.
   * @param l2regularizer
   *          L2 regularization weight.
   */
  public IntegerEffect(int id, double l1regularizer, double l2regularizer)
  {
    super(l1regularizer, l2regularizer);
    this.id = id;
  }

  /*
   * (non-Javadoc)
   * @see edu.cmu.cs.ark.sage.effects.Effect#getDescription()
   */
  @Override
  public String getDescription()
  {
    return Integer.toString(id);
  }

  /**
   * Hash code for this function is essentially just its <code>id</code>.
   * 
   * @see Object#hashCode()
   */
  @Override
  public int hashCode()
  {
    return id;
  }

  /**
   * Compares the <code>id</code> value of two {@link IntegerEffect}s for equality.
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

    IntegerEffect other = (IntegerEffect) obj;
    if (id != other.id)
      return false;

    return true;
  }
}
