package edu.cmu.cs.ark.sage.features;

/**
 * An abstract class that describes an observable feature of a document.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public abstract class Feature
{
  /*
   * (non-Javadoc)
   * @see java.lang.Object#toString()
   */
  @Override
  public String toString()
  {
    return String.format("Feature[%s]", hashCode());
  }
}
