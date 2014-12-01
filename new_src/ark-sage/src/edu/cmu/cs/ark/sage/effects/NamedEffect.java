package edu.cmu.cs.ark.sage.effects;

/**
 * This is an implementation of a SAGE {@link Effect} that is named, i.e it is indexed by a {@link String}.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class NamedEffect extends Effect
{
  private final String name;

  /**
   * Constructs a fixed effect with <code>name</code>.
   * 
   * @param name
   *          Name of this effect.
   */
  public NamedEffect(String name)
  {
    super();
    this.name = name;
  }

  /**
   * Constructs a non-fixed effect with <code>name</code> and L1 regularization.
   * 
   * @param name
   *          Name of this effect.
   * @param l1regularizer
   *          L1 regularization weight.
   */
  public NamedEffect(String name, double l1regularizer)
  {
    super(l1regularizer);
    this.name = name;
  }

  /**
   * Constructs a non-fixed effect with <code>name</code> and L1/L2 regularization.
   * 
   * @param name
   *          Name of this effect.
   * @param l1regularizer
   *          L1 regularization weight.
   * @param l2regularizer
   *          L2 regularization weight.
   */
  public NamedEffect(String name, double l1regularizer, double l2regularizer)
  {
    super(l1regularizer, l2regularizer);
    this.name = name;
  }

  /*
   * (non-Javadoc)
   * @see edu.cmu.cs.ark.sage.effects.Effect#getDescription()
   */
  @Override
  public String getDescription()
  {
    return name;
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#hashCode()
   */
  @Override
  public int hashCode()
  {
    return ((name == null) ? 0 : name.hashCode());
  }

  /**
   * Compares two {@link NamedEffect} using their <code>name</code>s.
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

    NamedEffect other = (NamedEffect) obj;
    if (name == null && other.name != null)
      return false;
    else if (!name.equals(other.name))
      return false;

    return true;
  }
}
