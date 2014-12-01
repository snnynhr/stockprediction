package edu.cmu.cs.ark.sage.apps;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map.Entry;

import org.apache.commons.math3.stat.StatUtils;
import org.apache.commons.math3.util.FastMath;

import edu.cmu.cs.ark.sage.SAGE;
import edu.cmu.cs.ark.sage.effects.Effect;
import edu.cmu.cs.ark.sage.effects.EffectSet;
import edu.cmu.cs.ark.sage.effects.NamedEffect;
import edu.cmu.cs.ark.sage.features.Feature;
import edu.cmu.cs.ark.sage.features.FeatureVector;
import edu.cmu.cs.ark.sage.features.UnigramFeature;
import edu.cmu.cs.ark.yc.utils.types.Pair;

/**
 * Very first version of SAGE demo app. Buggy now. Do not touch.
 * 
 * @deprecated
 * @author Yanchuan Sim
 * @version 0.1
 */
@Deprecated
public class HelloWorld
{
  /**
   * @param args
   *          the arguments to start the app off.
   * @throws IOException
   */
  public static void main(String[] args) throws IOException
  {
    SAGE S = new SAGE();

    BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream("input-word-counts.txt"), "UTF-8"));
    String line;

    Effect background = new Effect();
    S.addEffect(background);

    List<Pair<EffectSet, FeatureVector>> docs = new ArrayList<>();

    while ((line = br.readLine()) != null)
    {
      line = line.trim();
      if (line.isEmpty())
        continue;

      String[] fields = line.split("\t", 2);
      EffectSet doc_effects = new EffectSet();

      String[] effects_fields = fields[0].split(" ");
      boolean is_background_effect = false;

      doc_effects.add(background);

      for (String effects_field : effects_fields)
      {
        if (effects_field.isEmpty())
          continue;

        if (effects_field.equals("background"))
        {
          is_background_effect = true;
          continue;
        }

        NamedEffect e = new NamedEffect(effects_field, 1);
        S.addEffect(e);
        doc_effects.add(e);
      }
      if (!is_background_effect)
        S.addEffectSet(doc_effects);

      String[] wc_fields = fields[1].split(" ");
      FeatureVector doc = new FeatureVector();

      for (String wc : wc_fields)
      {
        String[] wc_arr = wc.split(":");
        UnigramFeature t = new UnigramFeature(wc_arr[0]);
        S.addFeature(t);
        doc.increment(t, Double.parseDouble(wc_arr[1]));
      }

      if (is_background_effect)
      {
      }
      else
        docs.add(new Pair<EffectSet, FeatureVector>(doc_effects, doc));
    }
    br.close();

    S.initialize(false);
    double[] bg_feature = new double[S.getFeatureList().size()];
    // double max_bg = -Double.MAX_VALUE;
    // for (Entry<Feature, Double> e : background_bow.entrySet())
    // {
    // bg_feature[S.findFeature(e.getKey())] = FastMath.log(e.getValue()) - FastMath.log(docs.size());
    // if (bg_feature[S.findFeature(e.getKey())] > max_bg)
    // max_bg = bg_feature[S.findFeature(e.getKey())];
    // }
    // for (int i = 0; i < S.getFeatureList().size(); i++)
    // bg_feature[i] -= max_bg;
    // S.setEta(background, bg_feature);

    for (Pair<EffectSet, FeatureVector> p : docs)
      for (Entry<Feature, Double> e : p.getB().entrySet())
        bg_feature[S.findFeature(e.getKey())] += e.getValue();

    for (int i = 0; i < bg_feature.length; i++)
      bg_feature[i] = FastMath.log(bg_feature[i]) - FastMath.log(docs.size());

    double max_bg = StatUtils.max(bg_feature);
    for (int i = 0; i < bg_feature.length; i++)
      bg_feature[i] -= max_bg;
    S.setEta(background, bg_feature);

    for (Pair<EffectSet, FeatureVector> p : docs)
      S.incrementFeatureVector(p.getA(), p.getB());

    S.setMaximumOWLQNIterations(100);
    S.prepareOptimization();
    for (Effect e : S.getEffectList())
    {
      S.optimizeEta(e);
    }
    S.print();
  }
}
