(ns sequdas_fulcro.client-test-main
  (:require sequdas_fulcro.tests-to-run
            [fulcro-spec.selectors :as sel]
            [fulcro-spec.suite :as suite]))

(enable-console-print!)

(suite/def-test-suite client-tests {:ns-regex #"sequdas_fulcro..*-spec"}
  {:default   #{::sel/none :focused}
   :available #{:focused}})

