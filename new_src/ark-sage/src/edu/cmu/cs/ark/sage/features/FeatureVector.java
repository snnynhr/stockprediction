package edu.cmu.cs.ark.sage.features;

import java.util.HashMap;

/**
 * A (sparse) vector of features and its corresponding values.
 * 
 * @author Yanchuan Sim
 * @version 0.1
 */
public class FeatureVector extends HashMap<Feature, Double>
{
  /**
   * version 0.1
   */
  private static final long serialVersionUID = 1L;

  /**
   * Increment the value of a particular feature in the vector.
   * 
   * @param feat
   *          Feature to increment the value of.
   * @param value
   *          Amount to increment by (or decrement if negative).
   * @return the updated feature value.
   */
  public Double increment(Feature feat, double value)
  {
    Double cur = this.get(feat);

    return this.put(feat, ((cur == null) ? value : cur + value));
  }

  /**
   * Returns the sum of absolute feature values.
   * 
   * @return the sum of absolute feature values.
   */
  public double l1_norm()
  {
    double sum = 0.0;
    for (Double c : this.values())
      sum += Math.abs(c);

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
    for (Double c : this.values())
      sum += c;

    return sum;
  }
}
