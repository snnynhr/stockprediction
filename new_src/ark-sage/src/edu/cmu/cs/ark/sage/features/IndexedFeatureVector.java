package edu.cmu.cs.ark.sage.features;

import gnu.trove.iterator.TIntDoubleIterator;
import gnu.trove.map.hash.TIntDoubleHashMap;

/**
 * Similar to {@link FeatureVector} by indexed by <code>int</code>s instead. Its based on {@link TIntDoubleHashMap} so it is fast.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class IndexedFeatureVector extends TIntDoubleHashMap
{
  /**
   * Increment the value of a particular feature in the vector.
   * 
   * @param key
   *          Feature index to increment the value of.
   * @param value
   *          Amount to increment by (or decrement if negative).
   */
  public void increment(int key, double value)
  {
    super.adjustOrPutValue(key, value, value);
  }

  /**
   * Returns the sum of absolute feature values.
   * 
   * @return the sum of absolute feature values.
   */
  public double l1_norm()
  {
    double sum = 0.0;
    for (TIntDoubleIterator it = this.iterator(); it.hasNext();)
    {
      it.advance();
      sum += Math.abs(it.value());
    }

    return sum;
  }

  /**
   * Returns the sum of feature values.
   * 
   * @return the sum of feature values.
   */
  public double sum()
  {
    double sum = 0.0;
    for (TIntDoubleIterator it = this.iterator(); it.hasNext();)
    {
      it.advance();
      sum += it.value();
    }

    return sum;
  }
}
