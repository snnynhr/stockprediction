package edu.cmu.cs.ark.yc.utils.types;

/**
 * A pretty standard Pair implementation that is not encouraged by Java or good programming practices.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class Pair<T1, T2>
{
  private T1 a;
  private T2 b;

  /**
   * Default constructor that does nothing.
   */
  public Pair()
  {
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#hashCode()
   */
  @Override
  public int hashCode()
  {
    final int prime = 31;
    int result = 1;
    result = prime * result + ((a == null) ? 0 : a.hashCode());
    result = prime * result + ((b == null) ? 0 : b.hashCode());
    return result;
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#equals(java.lang.Object)
   */
  @SuppressWarnings("unchecked")
  @Override
  public boolean equals(Object obj)
  {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (!(obj instanceof Pair<?, ?>))
      return false;

    Pair<T1, T2> other = (Pair<T1, T2>) obj;
    if (a == null && other.a != null)
      return false;
    else if (!a.equals(other.a))
      return false;

    if (b == null && other.b != null)
      return false;
    else if (!b.equals(other.b))
      return false;

    return true;
  }

  /**
   * Create a pair from given arguments <code>a</code> and <code>b</code>.
   * 
   * @param a
   *          Pair item <code>a</code>.
   * @param b
   *          Pair item <code>b</code>.
   */
  public Pair(T1 a, T2 b)
  {
    this.a = a;
    this.b = b;
  }

  /**
   * Returns the value of pair item <code>a</code>.
   * 
   * @return the value of pair item <code>a</code>.
   */
  public T1 getA()
  {
    return a;
  }

  /**
   * Sets the value of pair item <code>a</code>.
   * 
   * @param a
   *          The new value of pair item <code>a</code>.
   */
  public void setA(T1 a)
  {
    this.a = a;
  }

  /**
   * Returns the value of pair item <code>b</code>.
   * 
   * @return the value of pair item <code>b</code>.
   */
  public T2 getB()
  {
    return b;
  }

  /**
   * Sets the value of pair item <code>b</code>.
   * 
   * @param b
   *          The new value of pair item <code>b</code>.
   */
  public void setB(T2 b)
  {
    this.b = b;
  }

  /**
   * Sets both pair items value.
   * 
   * @param a
   *          The new value of pair item <code>a</code>.
   * @param b
   *          The new value of pair item <code>b</code>.
   */
  public void setPair(T1 a, T2 b)
  {
    this.a = a;
    this.b = b;
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString()
  {
    return "Pair[" + a + "," + b + "]";
  }
}
