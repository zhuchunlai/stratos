/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *  http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

package org.apache.stratos.cloud.controller.iaases.mock.statistics.generator;

import org.apache.stratos.cloud.controller.iaases.mock.MockAutoscalingFactor;

import java.util.Iterator;
import java.util.List;

/**
 * Mock health statistics pattern definition.
 */
public class MockHealthStatisticsPattern {
    private String cartridgeType;
    private MockAutoscalingFactor factor;
    private List<Integer> sampleValues;
    private int sampleDuration;
    private Iterator sampleValuesIterator;

    public MockHealthStatisticsPattern(String cartridgeType, MockAutoscalingFactor factor, List<Integer> sampleValues,
                                       int sampleDuration) {
        this.cartridgeType = cartridgeType;
        this.factor = factor;
        this.sampleValues = sampleValues;
        this.sampleValuesIterator = this.sampleValues.iterator();
        this.sampleDuration = sampleDuration;
    }

    public String getCartridgeType() {
        return cartridgeType;
    }

    /**
     * Returns autoscaling factor
     * @return
     */
    public MockAutoscalingFactor getFactor() {
        return factor;
    }

    /**
     * Returns next sample value
     * @return
     */
    public int getNextSample() {
        if(!sampleValuesIterator.hasNext()) {
            // Reset iterator
            sampleValuesIterator = sampleValues.iterator();
        }
        return Integer.parseInt(sampleValuesIterator.next().toString());
    }

    /**
     * Returns sample duration in seconds
     * @return
     */
    public int getSampleDuration() {
        return sampleDuration;
    }
}