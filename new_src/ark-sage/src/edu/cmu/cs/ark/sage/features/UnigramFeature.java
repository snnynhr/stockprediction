package edu.cmu.cs.ark.sage.features;

/**
 * An implementation of {@link Feature} for unigrams.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class UnigramFeature extends Feature
{
  /**
   * The type representing this unigram.
   */
  private final String type;

  /**
   * Constructs a unigram feature of <code>type</code>.
   * 
   * @param type
   *          The type-string of this unigram feature.
   */
  public UnigramFeature(String type)
  {
    this.type = type;
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString()
  {
    return type;
  }

  /*
   * (non-Javadoc)
   * @see java.lang.Object#hashCode()
   */
  @Override
  public int hashCode()
  {
    return ((type == null) ? 0 : type.hashCode());
  }

  /**
   * Compares equality by its <code>type</code> value.
   * 
   * @see java.lang.Object#equals(java.lang.Object)
   */
  @Override
  public boolean equals(Object obj)
  {
    if (this == obj)
      return true;
    if (obj == null)
      return false;

    if (getClass() != obj.getClass())
      return false;

    UnigramFeature other = (UnigramFeature) obj;
    if (type == null && other.type != null)
      return false;
    else if (!type.equals(other.type))
      return false;

    return true;
  }
}
